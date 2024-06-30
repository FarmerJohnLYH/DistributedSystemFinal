python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. pubsub.proto
python3 server.py
python3 client.py
