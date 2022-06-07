A tool to convert Markdown files to html applying CSS styles. Read more [from my blog](https://b3nsh4.com/blog/make-pdf-from-markdown-with-css-styles/)

![image](https://user-images.githubusercontent.com/22962287/172438313-d86bc1d1-2420-42fe-aabf-a01831169aa9.png)

## Usage
- ./md_resume_conv.py `file.md`
- ./md_resume_conv.py `file.md && firefox file.html`

## Convert HTML to PDF using Chrome/FireFox
- I suggest to use FireFox to make PDF (CTRL+P)
- Use chrome to make PDF out of our html file (CTRL+P)
- You can also use `chrome --headless` to make html to pdf from cli

## Footer
You can use `<i>` tag to add any footer/page numbers at the bottom of the page.

 Needful ref: https://developers.google.com/web/updates/2017/04/headless-chrome

This project is a fork of https://github.com/mikepqr/resume.md
