{
  description = "Python Development for Advent of Code";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixpkgs-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = inputs @ {
    self,
    nixpkgs,
    flake-utils,
    ...
  }:
    flake-utils.lib.eachDefaultSystem (system: let
      pkgs = import nixpkgs {inherit system;};
      envWithScript = script:
        (pkgs.buildFHSUserEnv {
          name = "python-env";
          targetPkgs = pkgs: (with pkgs; [
            python312
            python312Packages.pip
            python312Packages.virtualenv
            python312Packages.setuptools
            # Support binary wheels from PyPI
            pythonManylinuxPackages.manylinux2014Package
          ]);
          runScript = "${pkgs.writeShellScriptBin "runScript" (''
              set -e
              test -d .nix-venv || ${pkgs.python312.interpreter} -m venv .nix-venv
              source .nix-venv/bin/activate
              set +e

              pip install --editable .
            ''
            + script)}/bin/runScript";
        })
        .env;
    in {
      devShell = envWithScript "bash";
    });
}
