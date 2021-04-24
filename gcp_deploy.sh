project=$1
# image build
gcloud builds submit --tag asia.gcr.io/$project/streamlit-baseball

# deploy
gcloud run deploy --image asia.gcr.io/${project}/streamlit-baseball --platform managed --memory 512M
