##
# Local targets, meant to be run on the host machine
##

host ?= s_hidp_wagtail_sandbox@atlantis.leukeleu.nl

.PHONY: help
help:
	@echo "The following commands are meant to be run locally (i.e. not in a container):"
	@echo
	@echo "  make get-media - Get user uploaded media from staging"
	@echo "  make get-db - Get database from staging"
	@echo "  make clean - Remove virtualenv, node_modules, cache and other temporary files"
	@echo

.PHONY: get-media
get-media:
	rsync -avz --progress \
		${host}:/var/www/s_hidp_wagtail_sandbox/public/media/ \
		./var/public/media/

.PHONY: get-db
get-db:
	docker compose exec postgres dropdb -U postgres --if-exists --force postgres
	docker compose exec postgres createdb -U postgres postgres
	ssh ${host} pg_dump -cOx -Z9 | gunzip | docker compose exec -T postgres psql -U postgres

.PHONY: clean
clean:
	rm -rf var/venv var/cache var/*.sha1
	find . -type d -name node_modules | xargs rm -rf

.PHONY: install-git-hooks
install-git-hooks:
	mkdir -p .git/hooks
	ln -s ../../git-hooks/pre-push.sh .git/hooks/pre-push
	ln -s ../../git-hooks/pre-commit.sh .git/hooks/pre-commit

##
# This target is used by GitHub actions
##

.PHONY: release
release: export TAG = release-${GITHUB_RUN_NUMBER}
release: requirements = "../var/requirements_frozen.txt"
release: releasenotes = "[${TAG}](https://github.com/leukeleu/hidp_wagtail_sandbox/releases/tag/${TAG})"
release:
	git commit -m 'Make release' --allow-empty
	# Create and push release tag
	git tag $$TAG
	git push origin $$TAG

	# Clone leukeleu-ansible repo and create a new commits and pull requests in leukeleu-ansible
	git clone --depth 1 https://deployer:$$DEPLOYER_ACCESS_TOKEN@github.com/leukeleu/leukeleu-ansible.git
	$(MAKE) -C leukeleu-ansible release host=s_hidp_wagtail_sandbox requirements=${requirements} releasenotes=${releasenotes}
	$(MAKE) -C leukeleu-ansible release host=l_hidp_wagtail_sandbox requirements=${requirements} releasenotes=${releasenotes}
