<div align="center">
  <a href="https://github.com/jakub20kurdziel/ceneo-scraper">
    <img src="https://raw.githubusercontent.com/othneildrew/Best-README-Template/master/images/logo.png" alt="Logo" width="80" height="80">
  </a>
  
  <h3 align="center">Ceneo scraper</h3>

  <p align="center">
     Application to extract opinions from Ceneo.pl website.
    <br />
  </p>
</div>


<div align="center">

<a href="https://github.com/kubo550/ceneo-scraper/stargazers"><img src="https://img.shields.io/github/stars/kubo550/ceneo-scraper" alt="Stars Badge"/></a>
<a href="https://github.com/kubo550/ceneo-scraper/network/members"><img src="https://img.shields.io/github/forks/kubo550/ceneo-scraper" alt="Forks Badge"/></a>
<a href="https://github.com/kubo550/ceneo-scraper/pulls"><img src="https://img.shields.io/github/issues-pr/kubo550/ceneo-scraper" alt="Pull Requests Badge"/></a>
<a href="https://github.com/kubo550/ceneo-scraper/issues"><img src="https://img.shields.io/github/issues/kubo550/ceneo-scraper" alt="Issues Badge"/></a>
<a href="https://github.com/kubo550/ceneo-scraper/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/kubo550/ceneo-scraper?color=2b9348"></a>
<a href="https://github.com/kubo550/ceneo-scraper/blob/master/LICENSE"><img src="https://img.shields.io/github/license/kubo550/ceneo-scraper?color=2b9348" alt="License Badge"/></a>

</div>

<!-- GETTING STARTED -->

## :book: Description

|Składowa|Selektor|Zmienna|
|--------|--------|-------|
|opinia|div.js_product-review|review|
|identyfikator opinii|\[data-entry-id\]|review_id|
|autor|span.user-post__author-name|author|
|rekomendacja|span.user-post__author-recomendation > em|recommendation|
|liczba gwiazdek|span.user-post__score-count|stars|
|treść|div.user-post__text|content|
|data wystawienia|span.user-post__published > time:nth-child(1)\[datetime\]|publish_date|
|data zakupu|span.user-post__published > time:nth-child(2)\[datetime\]|purchase_date|
|dla ilu przydatna|button.vote-yes[data-total-vote]<br>button.vote-yes > span<br>span[id^=votes-yes]|useful|
|dla ilu nieprzydatna|button.vote-no[data-total-vote]<br>button.vote-no > span<br>span[id^=votes-no]|useless|
|lista zalet|div.review-feature__title--positives ~ div.review-feature__item <br>div.review-feature__col:has( > div.review-feature__title--positives) > div.review-feature__item<br>div.review-feature__item:has( ~ div.review-feature__title--positives)|pros|
|lista wad|div.review-feature__title--negatives ~ div.review-feature__item <br>div.review-feature__col:has( > div.review-feature__title--negatives) > div.review-feature__item<br>div.review-feature__item:has( ~ div.review-feature__title--negatives)|cons|

## :runner: Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### :arrow_down: Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Clone the repo
   ```sh
   git clone git@github.com:jakub20kurdziel/ceneo-scraper.git
   ```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- about -->

## :information_source: About

Object Oriented Programming

## 👀 Preview

<img src="https://raw.githubusercontent.com/kubo550/ceneo-scraper/master/gh/preview.png" alt="preview" />

## :rocket: Tech Stack

- Python
- BeautifulSoup
- Bootstrap
- Flask
- Chart.js
- Jsonpickle
- Datatables
- Icons8

## :computer: Usage

Open repo in new terminal widnow

`source flask/bin/activate`

`python app.py`

then go to [http://localhost:5000/](http://localhost:5000/) in your browser

<p align="right">(<a href="#top">back to top</a>)</p>

## :exclamation: Important Note

Make sure you have disabled VPN before running the app. Ceneo.pl website is blocked by VPN. You can find more information about VPN [here](https://www.vpnbook.com/freevpn).

## :pencil: License

This project is licensed under [MIT](https://opensource.org/licenses/MIT) license.

## :man_astronaut: Show your support

Give a ⭐️ if this project helped you!

