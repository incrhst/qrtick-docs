# Makefile for QRTick Fee Calculator Vite Project

install:
	npm install

build:
	npm run build

rename:
	cp dist/index.html dist/fee-calculator.html

copy:
	cp dist/fee-calculator.html ./fee-calculator.html
	@if [ -d dist/assets ]; then cp -r dist/assets ./assets; fi

deploy: build rename copy

all: install deploy

.PHONY: install build rename copy deploy all 