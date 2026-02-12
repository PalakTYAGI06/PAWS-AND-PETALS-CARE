
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
import cv2
from django.http import StreamingHttpResponse

from django.contrib.auth import get_user_model

User = get_user_model()

def register_view(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        role = request.POST.get("role")

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect("register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect("register")

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password1
        )
        user.full_name = full_name
        user.role = role
        user.save()

        messages.success(request, "Account created successfully")
        login(request, user)
        return redirect("plan")

    return render(request, "register.html")
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('camera_page')
        else:
            messages.error(request, "Invalid credentials")
    return render(request, 'live.login.html')

def plan_page(request):
    return render(request, 'plan.html')

def gen_frames():
    cap = cv2.VideoCapture(0)
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')

def camera_page(request):
    return render(request,'live.html')
    return StreamingHttpResponse(gen_frames(), content_type='multipart/x-mixed-replace; boundary=frame')
def home(request):
    return render(request, 'home.html')
from django.shortcuts import render

def plan_page(request):
    return render(request, 'plan.html')

def services_page(request):
    return render(request, 'services.html')
def service(request):
    return render(request, 'service.html')
def care(request):
    return render(request, 'care.html')










# Create your views here.
# camera/views.py
from django.shortcuts import render, redirect
from django.http import StreamingHttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.gzip import gzip_page
from django.core.files.base import ContentFile
from .models import Snapshot
import cv2, base64
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout

# Camera source: 0 for local webcam OR RTSP URL for IP camera
CAMERA_SOURCE = 0
# Example: CAMERA_SOURCE = "rtsp://username:password@192.168.1.10:554/stream"

def frame_generator():
    """Generator that yields camera frames as JPEG for streaming."""
    cap = cv2.VideoCapture(CAMERA_SOURCE)
    if not cap.isOpened():
        raise RuntimeError("Could not open camera source")

    while True:
        success, frame = cap.read()
        if not success:
            break
        ret, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@gzip_page
@login_required
def live_feed(request):
    """Stream live camera feed as MJPEG."""
    return StreamingHttpResponse(frame_generator(),
        content_type='multipart/x-mixed-replace; boundary=frame')

@login_required
def live_page(request):
    """Render the live camera page with recent snapshots."""
    snapshots = Snapshot.objects.order_by('-created_at')[:12]
    return render(request, 'templates/live.html', {'snapshots': snapshots})

@login_required
def save_snapshot(request):
    """Save a snapshot from the live feed into the database."""
    if request.method == 'POST':
        data_url = request.POST.get('image')
        note = request.POST.get('note', '')

        if not data_url or not data_url.startswith('data:image/jpeg;base64,'):
            return JsonResponse({'ok': False, 'error': 'Invalid image data'}, status=400)

        # Decode base64 image
        b64 = data_url.split(',')[1]
        image_bytes = base64.b64decode(b64)

        snap = Snapshot()
        snap.image.save('snapshot.jpg', ContentFile(image_bytes), save=True)
        snap.note = note
        snap.save()

        return JsonResponse({'ok': True})

    return JsonResponse({'ok': False, 'error': 'POST required'}, status=405)

#def register(request):
   # if request.method == 'POST':
      #  form = UserCreationForm(request.POST)
      #  if form.is_valid():
       #     user = form.save()
       ##     login(request, user)  #auto login after registration
          #  return redirect('live_page')
   # else:
     ##   form = UserCreationForm()
    #return render(request, 'registration/register.html', {'form': form})
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('live_page')
    else:
        form = AuthenticationForm()
    return render(request, 'templates/live.login.html', {'form': form})
def user_logout(request):
    logout(request)
    return redirect('live.login')
#feeback#


from django.core.mail import send_mail
from .models import Feedback

def feedback_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save to database
        feedback = Feedback.objects.create(name=name, email=email, message=message)

        # Send email to Gmail
        send_mail(
            subject=f"New Feedback from {feedback.name}",
            message=f"Email: {feedback.email}\n\nMessage:\n{feedback.message}",
            from_email='riyaverma9067@gmail.com',   # replace with your Gmail
            recipient_list=['riyaverma9067@gmail.com'], # replace with your Gmail
            fail_silently=False,
        )

        return redirect('feedback_success')

    return render(request, 'feedback.html')

def feedback_success(request):
    return render(request, 'feedback_success.html')