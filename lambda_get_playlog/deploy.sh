# A simple packaging script. This will create a zip (deploy.zip) which can be
# uploaded to AWS Lambda

echo "Creating deployment package"

mkdir deploy

echo "Copying source (/src) files"
cp -r src/* deploy

echo "Copying virtualenv (/env) files"
cp -r env/* deploy

echo "Zipping..."
cd deploy
zip -r ../deploy.zip .
cd ..

echo "Cleaning up"
rm -rf deploy

echo "Done"
