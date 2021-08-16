import sys
sys.path.append('./proto')
sys.path.append('./grpc_packages/user_center')
sys.path.append('./handler')
sys.path.append('./dal/db')

import user_center_pb2 as UserCenter
import user_center_pb2_grpc as UserCentergrpc
import userhandler as Uhan
import mysql as sqlnet
import grpc
from concurrent import futures

class UserCenterHandler(UserCentergrpc.UserCenterServicer):
    def __init__(self):
        sqlnet.connectMysql()

    def Register(self, request, context):
        return Uhan.Register(request, context)

    def Login(self, request, context):
        return Uhan.Login(request, context)

    def Delete(self, request, context):
        return Uhan.Delete(request, context)

    def CheckToken(self, request, context):
        return Uhan.CheckToken(request, context)

    def Refresh(self, request, context):
        return Uhan.Refresh(request, context)

    def GetUserInfo(self, request, context):
        return Uhan.GetUserInfo(request, context)

    def AddUser(self, request, context):
        return Uhan.AddUser(request, context)


if __name__ == "__main__":
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    UserCentergrpc.add_UserCenterServicer_to_server(
        UserCenterHandler(), server)
    server.add_insecure_port('[::]:9999')
    server.start()
    print("Starting python server...")
    server.wait_for_termination()
