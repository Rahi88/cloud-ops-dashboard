from flask import Flask, jsonify
from flask_cors import CORS
import boto3

app = Flask(__name__)
CORS(app)  # Unlocks the security gate for your web browser interface

# 1. PASTE YOUR ACTUAL UBUNTU INSTANCE ID HERE
INSTANCE_ID = "i-00xxxxxxxxxxx" 

# 2. Setting up the Boto3 EC2 client (us-east-1 for N. Virginia)
ec2 = boto3.client('ec2', region_name='us-east-1')

#method to start server
@app.route('/start-server', methods=['POST'])
def start_server():
    try:
        # Boto3 core command to turn ON an EC2 instance
        ec2.start_instances(InstanceIds=[INSTANCE_ID])
        return jsonify({"status": "success", "message": f"Server {INSTANCE_ID} start command issued!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

#method to stop server
@app.route('/stop-server', methods=['POST'])
def stop_server():
    try:
        # Boto3 core command to turn OFF an EC2 instance
        ec2.stop_instances(InstanceIds=[INSTANCE_ID])
        return jsonify({"status": "success", "message": f"Server {INSTANCE_ID} stop command issued!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400
        
#method to terminate server
@app.route('/terminate-server', methods=['POST'])
def terminate_server():
    try:
        # Boto3 core command to turn OFF an EC2 instance
        ec2.terminate_instances(InstanceIds=[INSTANCE_ID])
        return jsonify({"status": "success", "message": f"Server {INSTANCE_ID} terminate command issued!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == '__main__':
    print("DevOps Portal Backend is booting up on http://localhost:5000")
    app.run(port=5000, debug=True)
