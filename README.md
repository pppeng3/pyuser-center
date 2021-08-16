python3 -m grpc_tools.protoc -I=./proto --python_out=./grpc_packages --grpc_python_out=./grpc_packages ./proto/base/base.proto

python3 -m grpc_tools.protoc -I=./proto --python_out=./grpc_packages --grpc_python_out=./grpc_packages  ./proto/user-center/user-center.proto

python3 -m grpc_tools.protoc -I=./proto --python_out=./grpc_packages --grpc_python_out=./grpc_packages  proto/*/*.proto