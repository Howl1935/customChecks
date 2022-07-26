config {
  disabled_by_default = false
  # other options here...
}
plugin "aws" {
    enabled = true
    version = "0.15.0"
    source  = "github.com/terraform-linters/tflint-ruleset-aws"
}