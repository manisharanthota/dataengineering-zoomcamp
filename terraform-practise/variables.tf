variable "project_id" {
  description = "Project ID"
  default     = "tf-practise-487222"

}

variable "credentials" {
  description = "Link of File to Credentials"
  default     = "./keys/keys.json"

}

variable "region" {
  description = "region(different from location)"
  default     = "us-central1"

}

variable "location" {
  description = "Project Location"
  default     = "US"

}

variable "bucket_name" {
  description = "Name of the bucket"
  default     = "tf-practise-487222-terra-bucket"

}

variable "dataset_id" {
  description = "Id of the dataset"
  default     = "demo_dataset"

}