# Makefile for QRTick Fee Calculator Vite Project

install:
	npm install

build:
	cd fee-calculator-vite && npm run build

rename:
	cp dist/index.html dist/fee-calculator.html

copy:
	cp fee-calculator-vite/dist/index.html ./fee-calculator.html
	@if [ -d fee-calculator-vite/dist/assets ]; then cp -r fee-calculator-vite/dist/assets ./assets; fi

deploy: build copy

all: install deploy

.PHONY: install build rename copy deploy all 