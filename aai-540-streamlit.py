# AAI-540 Group-4
import streamlit as st
import boto3

# AWS credentials and SageMaker endpoint name
aws_access_key_id = 'AKIARUKCDJHBH3SAOGAA'
aws_secret_access_key = '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'
region_name = 'us-east-1'
endpoint_name = 'hf-distilbert-QA-string-endpoint'

# Initialize boto3 client
sagemaker_client = boto3.client('sagemaker-runtime',
                         aws_access_key_id=aws_access_key_id,
                         aws_secret_access_key=aws_secret_access_key,
                         region_name=region_name)

# Streamlit UI
st.title('AI-540 Group-4')
st.divider()
st.markdown('## Question Answering System')

def invoke_sagemaker_endpoint(question, context):
    test_text = "|".join((question, context))

    response = sagemaker_client.invoke_endpoint(
        EndpointName=endpoint_name,
        Body=test_text,
        ContentType='text/plain',  # or the appropriate content type for your model
    )

    prediction = response['Body'].read().decode('utf-8').strip('"')
    return prediction


amzn_question = st.text_input("Enter your question:", "")
amzn_context = st.text_area("Enter the context:", "")

if st.button('Predict Answer'):
    prediction = invoke_sagemaker_endpoint(amzn_question, amzn_context)
    st.write(f"Answer: {prediction}")
~                                            
