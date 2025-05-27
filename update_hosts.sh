#!/bin/bash

# Get the Vagrant VM IP
VM_IP=$(vagrant ssh -c "hostname -I" | tr -d '[:space:]')
VM_NAME=$(vagrant ssh -c "hostname" | tr -d '[:space:]')

# Check if variables are set
if [ -z "${VM_IP}" ] || [ -z "${VM_NAME}" ]; then
    echo "Error: VM_IP or VM_NAME not set"
    exit 1
fi


echo "Checking for existing host entry..."
if sudo grep -q "${VM_NAME}" /etc/hosts; then
    echo "Removing existing entry for ${VM_NAME}..."
    sudo sed -i '' "/${VM_NAME}/d" /etc/hosts
fi
# update /etc/hosts
echo "adding entry to /etc/hosts..."
sudo bash -c "echo ${VM_IP} ${VM_NAME} >> /etc/hosts"

# Update Ansible inventory
echo "Updating Ansible inventory..."
cat > hosts << EOF
[${VM_NAME}]
${VM_IP} ansible_user=ansible
EOF

echo "Done! You can now access the VM using: $VM_NAME"
