from label_image import main_func
from output_form import display_form
import cv2

model_file = "D:/Temp/Animals/Code/output_graph.pb"

model_file = "D:\\Work\\Neural Network\\Animal Classification\\output_graph.pb"
label_file = "D:\\Work\\Neural Network\\Animal Classification\\output_labels.txt"
input_height = 299
input_width = 299
input_mean = 0  
input_std = 255
input_layer = "Placeholder"
output_layer = "final_result"


cap = cv2.VideoCapture(0)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    cv2.imwrite('frame.jpg', frame)
    if cv2.waitKey(1) & 0xFF == ord('c'):
        labels, results, top_k = main_func("frame.jpg", model_file, label_file, input_height, input_width,
                                           input_mean, input_std, input_layer, output_layer)

        display_form(labels, results, top_k)
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()