import cv2
import time

def main():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return
    
    # Face tracking variables
    last_face_time = time.time()
    face_missing_threshold = 3.0  # 3 seconds
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        current_time = time.time()
        
        if len(faces) > 0:
            # Face detected - reset timer and draw rectangles
            last_face_time = current_time
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        else:
            # No face - check if missing > 3 seconds
            if current_time - last_face_time > face_missing_threshold:
                cv2.putText(frame, 'FACE MISSING', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 
                           1.2, (0, 0, 255), 3)
                print("FACE MISSING")
        
        cv2.imshow('Face Detection', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()