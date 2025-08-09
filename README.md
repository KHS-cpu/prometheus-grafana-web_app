# Prometheus & Grafana Monitoring on AWS EC2
This repository contains the core code and configuration files for a monitoring project where Prometheus and Grafana are deployed on separate AWS EC2 instances. The goal is to monitor a simple Flask-based web server running on its own EC2 instance by scraping custom metrics exposed at /metrics.

## Project Diagram

## Key features of this lab include:
- Deploying Prometheus on an EC2 instance to scrape metrics from the web server.
- Setting up Grafana on a separate EC2 instance for creating dashboards and visualizing metrics.
- Integrating PagerDuty with Grafana for real-time alerting.
- Using Docker and Docker Compose on all instances for easy deployment and management.

  Note: Much of the configuration work — such as building Grafana dashboards, setting up alert rules, and PagerDuty integration — is done via the Grafana web UI. Therefore, this repository contains mostly code related to the web server, Prometheus configuration, and Docker Compose files.

  For a detailed step-by-step tutorial, complete with screenshots, explanations, and architectural insights, please visit my blog:
  https://blogs.kaunghtetsan.tech/prometheus-and-grafana-monitoring-web-server-with-docker-on-aws-ec2

  Feel free to clone, experiment, and reach out if you have any questions!
