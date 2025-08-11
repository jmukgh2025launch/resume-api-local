from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def resume():
    skills = {
        "name": "Josh Medrano",
        "role": "Azure Cloud Platform Engineer / Junior Cloud Engineer",
        "skills": {
            "Cloud Platforms": ["Azure (VMs, Storage, Networking, IAM)"],
            "Infrastructure as Code": ["Terraform (modules, state management, provisioning)"],
            "Containers": ["Docker (image creation, container management)", "Basic Kubernetes"],
            "CI/CD": ["GitHub Actions", "Azure DevOps Pipelines"],
            "IT Support": [
                "Desktop user support & common issues",
                "Basic network issues",
                "On-site experience face-to-face & on-call for clients"
                "User device setup & maintenance",
                "Active Directory; User account & permissions management"
            ],
            "Operating Systems": ["Linux (CLI, permissions, services)", "Windows Server basics"]
        },
        "projects": [
            "Python ordering system for fictional cafe",
            "Provisioned cloud infrastructure using Terraform",
            "Set up automated deployments with GitHub Actions",
            "Small basic network setup in Azure with VMs"
        ],
        "contact": {
            "GitHub": "https://github.com/jmukgh2025launch",
            "LinkedIn": "https://linkedin.com/in/josh-medrano-ab7747ab"
        }
    }
    return jsonify(skills)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)



#Original app.py code >>>

#from flask import Flask
#app = Flask(__name__)

#@app.route("/")
#def resume():
    #return "Hello, this is my resume API!"

#if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=5000)
