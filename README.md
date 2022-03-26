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

<a href="https://github.com/jakub20kurdziel/ceneo-scraper/stargazers"><img src="https://img.shields.io/github/stars/jakub20kurdziel/ceneo-scraper" alt="Stars Badge"/></a>
<a href="https://github.com/jakub20kurdziel/ceneo-scraper/network/members"><img src="https://img.shields.io/github/forks/jakub20kurdziel/ceneo-scraper" alt="Forks Badge"/></a>
<a href="https://github.com/jakub20kurdziel/ceneo-scraper/pulls"><img src="https://img.shields.io/github/issues-pr/jakub20kurdziel/ceneo-scraper" alt="Pull Requests Badge"/></a>
<a href="https://github.com/jakub20kurdziel/ceneo-scraper/issues"><img src="https://img.shields.io/github/issues/jakub20kurdziel/ceneo-scraper" alt="Issues Badge"/></a>
<a href="https://github.com/jakub20kurdziel/ceneo-scraper/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/jakub20kurdziel/ceneo-scraper?color=2b9348"></a>
<a href="https://github.com/elangosundar/awesome-README-templates/blob/master/LICENSE"><img src="https://img.shields.io/github/license/jakub20kurdziel/ceneo-scraper?color=2b9348" alt="License Badge"/></a>

</div>

<!-- GETTING STARTED -->

## :book: Description

| Składowa             | Selektor                                                    | Zmienna       |
| -------------------- | ----------------------------------------------------------- | ------------- |
| opinia               | div.js_product-review                                       | review        |
| id opinii            | div.js_product-review\[data-entry-id\]                      | review_id     |
| autor                | .user-post\_\_author-name                                   | author        |
| rekomendacja         | .user-post\_\_author-recomendation > em                     | recomendation |
| liczba gwiazdek      | .user-post\_\_score-count                                   | score_count   |
| treść                | .user-post\_\_text                                          | content       |
| data wystawienia     | span.user-post\_\_published > time\[datetime\]:nth-child(1) | publish_date  |
| data zakupu          | span.user-post\_\_published > time\[datetime\]:nth-child(2) | purchase_date |
| dla ilu przydatna    |                                                             | useful        |
| dla ilu nieprzydatna |                                                             | useless       |
| liczba zalet         | review-feature                                              | pros          |
| liczba wad           | review-feature                                              | cons          |

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

## :pencil: License

This project is licensed under [MIT](https://opensource.org/licenses/MIT) license.

## :man_astronaut: Show your support

Give a ⭐️ if this project helped you!
