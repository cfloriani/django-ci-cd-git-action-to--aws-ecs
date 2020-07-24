#!/usr/bin/env python3

from aws_cdk import core

from ecs_sks_cdk.ecs_sks_cdk_stack import EcsSksCdkStack


app = core.App()
EcsSksCdkStack(app, "ecs-sks-cdk")

app.synth()
