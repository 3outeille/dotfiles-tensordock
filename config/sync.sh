#!/bin/sh

# Function to display usage information
display_usage() {
  printf "Usage: %s <mode> <ssh_port> <source_path> <destination_path>\n" "$0"
  printf "Modes:\n"
  printf "  - to-local: Copy from remote to local.\n"
  printf "  - to-ssh: Copy from local to remote.\n"
  printf "Example (to-local): %s to-local 10292 /remote/source/directory /local/destination/directory/\n" "$0"
  printf "Example (to-ssh): %s to-ssh 10292 /local/source/directory /remote/destination/directory/\n" "$0"
}

# Check if the correct number of arguments are provided
if [ "$#" -ne 4 ]; then
  display_usage
  exit 1
fi

mode="$1"

if [ "$mode" != "to-local" ] && [ "$mode" != "to-ssh" ]; then
  printf "Invalid mode. Use 'to-local' or 'to-ssh'.\n"
  display_usage
  exit 1
fi

ssh_port="$2"  # SSH port number to connect to the remote server.
source_path="$3"  # Source path (local or remote).
destination_path="$4"  # Destination path (local or remote).

if [ "$mode" = "to-local" ]; then
  # Copy from remote to local
  rsync -arlptP --append-verify -e "ssh -p $ssh_port" "$source_path" "$destination_path"
elif [ "$mode" = "to-ssh" ]; then
  # Copy from local to remote
  rsync -arlptP --append-verify -e "ssh -p $ssh_port" "$source_path" "$destination_path"
fi
