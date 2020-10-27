import glob, os
# Current directory
current_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir)
train_dir = '/home/tian/Projects/OIDv4_ToolKit/OID/Dataset/train/Dinosaur'
test_dir = '/home/tian/Projects/OIDv4_ToolKit/OID/Dataset/test/Dinosaur'
file_train = open('train.txt', 'w')  
file_test = open('test.txt', 'w')

for pathAndFilename in glob.iglob(os.path.join(train_dir, "*.jpg")):  
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    file_train.write('/home/tian/PyTorch-YOLOv3/data/custom/images' + "/" + title + '.jpg' + "\n")

for pathAndFilename in glob.iglob(os.path.join(test_dir, "*.jpg")):  
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    file_test.write('/home/tian/PyTorch-YOLOv3/data/custom/images' + "/" + title + '.jpg' + "\n")
