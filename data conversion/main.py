

# from google.api_core.client_options import ClientOptions
# from google.cloud import documentai

# # TODO(developer): Uncomment these variables before running the sample.
# project_id = 'document-ai-371007'
# location = 'eu' # Format is 'us' or 'eu'
# processor_id = '97db5db78c32d129' #  Create processor before running sample
# file_path = 'D:\projects\conversion\google\doc\page1.pdf'
# mime_type = 'application/pdf' # Refer to https://cloud.google.com/document-ai/docs/file-types for supported file types


# def quickstart(
#     project_id: str, location: str, processor_id: str, file_path: str, mime_type: str
# ):
#     # You must set the api_endpoint if you use a location other than 'us', e.g.:
#     opts = ClientOptions(api_endpoint=f"{location}-documentai.googleapis.com")

#     client = documentai.DocumentProcessorServiceClient(client_options=opts)

#     # The full resource name of the processor, e.g.:
#     # projects/project_id/locations/location/processor/processor_id
#     name = client.processor_path(project_id, location, processor_id)

#     # Read the file into memory
#     with open(file_path, "rb") as image:
#         image_content = image.read()

#     # Load Binary Data into Document AI RawDocument Object
#     raw_document = documentai.RawDocument(content=image_content, mime_type=mime_type)

#     # Configure the process request
#     request = documentai.ProcessRequest(name=name, raw_document=raw_document)

#     result = client.process_document(request=request)

#     # For a full list of Document object attributes, please reference this page:
#     # https://cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.Document
#     document = result.document

#     # Read the text recognition output from the processor
#     print("The document contains the following text:")
#     print(document.text)

# quickstart(project_id, location, processor_id, file_path, mime_type)
d=0
for i in range(9):
    print(d)
    d=d+1
