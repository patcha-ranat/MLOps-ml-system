terraform {
  required_version = "~> 1.5.3"
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 4.12.0"
    }
  }
  backend "azurerm" {
    # Variables not allowed
    resource_group_name  = "tfstate"
    storage_account_name = "tfstatesakmlops"
    container_name       = "tfstatesckmlops"
    key                  = "terraform.tfstate"
  }
}

# Configure the Microsoft Azure Provider

provider "azurerm" {
  features {}

  subscription_id = var.subscription_id
  client_id       = var.client_id
  client_secret   = var.client_secret
  tenant_id       = var.tenant_id
}

# Resource Group

resource "azurerm_resource_group" "resource_group" {
  name     = var.resource_group_name
  location = var.location
}

# Web App / App Service
# service plan
resource "azurerm_service_plan" "service_plan" {
  name                = "app-service-plan-${azurerm_resource_group.resource_group.name}-${azurerm_resource_group.resource_group.location}" # to be unique name
  resource_group_name = azurerm_resource_group.resource_group.name
  location            = azurerm_resource_group.resource_group.location
  os_type             = var.service_plan_os_type
  sku_name            = var.service_plan_sku_name
}
# web app
resource "azurerm_linux_web_app" "web_app" {
  name                = var.web_app_name
  resource_group_name = azurerm_resource_group.resource_group.name
  location            = azurerm_service_plan.service_plan.location
  service_plan_id     = azurerm_service_plan.service_plan.id

  site_config {
    application_stack {
      docker_image_name   = var.web_app_docker_image_name
      docker_registry_url = var.web_app_docker_registry_url
    }

    always_on = var.web_app_always_on
  }
}