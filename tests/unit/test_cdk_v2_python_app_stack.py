import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_v2_python_app.cdk_v2_python_app_stack import CdkV2PythonAppStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_v2_python_app/cdk_v2_python_app_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkV2PythonAppStack(app, "cdk-v2-python-app")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
