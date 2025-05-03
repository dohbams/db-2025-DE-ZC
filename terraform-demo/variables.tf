variable "project" {
  description = "Project Name"
  default     = "bigquery-portfolio"
}

variable "region" {
  description = "Project Region"
  default     = "europe-west1"
}


variable "location" {
  description = "Project Location"
  default     = "EU"
}

variable "credentials" {
  description = "Credentials"
  default =  "./keys/keys.json"
  sensitive = true
}



variable "bq_dataset_name" {
  description = "Dataset Name"
  default     = "tf_demo_dataset"
}

variable "gcs_bucket_name" {
  description = "Bucket Name"
  default     = "bigquery-portfolio-tf-demo-bucket"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}