from typing import Any
from aws_cdk import (
    Stack,
    aws_iam as iam,
)
from constructs import Construct

class CdkRoleBugExampleStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs: Any) -> None:
        super().__init__(scope, construct_id, **kwargs)

        role: iam.IRole = iam.Role(
            self,
            'testRole',
            assumed_by=iam.ServicePrincipal("batch.amazonaws.com")
        )

        print(role)