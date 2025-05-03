terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "6.26.0"
    }
  }
}

provider "google" {
  # Configuration options
  project = var.project
  region  = var.region
  credentials = file(var.credentials)
}

resource "google_storage_bucket" "tf-demo-bucket" {
  name                     = var.gcs_bucket_name
  location                 = var.location
  storage_class            = var.gcs_storage_class
  force_destroy            = true
  public_access_prevention = "enforced"

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}

resource "google_bigquery_dataset" "tf_demo_dataset" {
  dataset_id = var.bq_dataset_name
  location   = var.location
}