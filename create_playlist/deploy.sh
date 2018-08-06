# A simple packaging script. This will create a zip (deploy.zip) which can be
# uploaded to AWS Lambda

echo "Creating deployment package"

mkdir deploy

echo "Copying source files (/src)"
cp -r src/. deploy # copy hidden files as well

echo "Copying virtualenv libraries (/env/lib/python3.6/site-packages)"
cp -r env/lib/python3.6/site-packages/* deploy

echo "Zipping..."
cd deploy
zip -r ../deploy.zip .
cd ..

echo "Cleaning up"
rm -rf deploy

echo "Done"
