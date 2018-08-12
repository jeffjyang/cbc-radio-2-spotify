# A simple AWS Lambda deployment script 

echo "Enter target AWS Lambda function name:"
read function_name 

echo "Creating deployment package..."
mkdir deploy

echo "Copying source files (/src)..."
cp -r src/. deploy # copy hidden files as well

echo "Copying libraries (/env/lib/python3.6/site-packages)..."
cp -r env/lib/python3.6/site-packages/* deploy

echo "Zipping..."
cd deploy
zip -r ../deploy.zip .
cd ..

echo "Deploying..."
aws lambda update-function-code \
--function-name $function_name \
--zip-file fileb://deploy.zip

echo "Cleaning up..."
rm -rf deploy
rm deploy.zip

echo "Done"

