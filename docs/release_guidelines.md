# OCS-CI Releases

OCS-CI releases are generated in conjunction with OCS releases, A release is cut
as soon as OCS is Generally Availabled and available in open market place.

The release helps to checkout specific versions of tests that were run during
the release and serves as baseline for the specific version of OCS.

# Release Process
1. Create a tag specific to commit that matches the latest ocs-ci that was used to run
the regression tests. 
2. Update the setup.py to match the ocs version. 
3. Update the release notes to highlight changes that went in the ocs-ci repo
4. Generate the release