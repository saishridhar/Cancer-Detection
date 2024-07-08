# Cancer-Detection
Web app that allows you to upload X-ray images to classify Lung Cancer

mlflow server -h 0.0.0.0 --default-artifact-root s3://mlflowbuc1
export MLFLOW_TRACKING_URI = http://ec2-18-188-232-57.us-east-2.compute.amazonaws.com:5000/