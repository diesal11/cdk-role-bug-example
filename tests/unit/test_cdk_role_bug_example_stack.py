import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_role_bug_example.cdk_role_bug_example_stack import CdkRoleBugExampleStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_role_bug_example/cdk_role_bug_example_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkRoleBugExampleStack(app, "cdk-role-bug-example")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
