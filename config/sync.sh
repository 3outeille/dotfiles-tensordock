#!/bin/sh

# Function to display usage information
display_usage() {
  printf "SHOULD BE USE IN LOCAL computer (not on remote SSH)\n" "$0"
  printf "Usage: %s <ssh_port> <source_path> <destination_path>\n" "$0"
  printf "Example: %s to-local 10292 /remote/source/directory /local/destination/directory/\n" "$0"
}

# Check if the correct number of arguments are provided
if [ "$#" -ne 3 ]; then
  display_usage
  exit 1
fi

ssh_port="$1"  # SSH port number to connect to the remote server.
source_path="$2"  # Source path (local or remote).
destination_path="$3"  # Destination path (local or remote).

rsync -arlptP --stats --append-verify -e "ssh -p $ssh_port" "$source_path" "$destination_path"
