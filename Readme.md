<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** dimamik, what-to-read, twitter_handle, email, What To Read, project_description
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/dimamik/what-to-read">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">What To Read</h3>

  <p align="center">
    Single Page Application designed to help you find a book to read having books you have read previously.<br /> 
    Based on <a href=https://en.wikipedia.org/wiki/Collaborative_filtering> Collaborative filtering</a> technique
    <br />
    <!-- <a href="https://github.com/dimamik/what-to-read"><strong>Explore the docs »</strong></a>
    <br /> -->
    <br />
    <a href="https://github.com/dimamik/what-to-read">View Demo</a>
    ·
    <a href="https://github.com/dimamik/what-to-read/issues">Report Bug</a>
    ·
    <a href="https://github.com/dimamik/what-to-read/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

## Project Structure
<pre>
├──nginx - reversed proxy
├── ui - React Front
├── rec_api - REST API server handling recommendations
├── search_api - REST API server handling books searching
└── img - images for Readme.md
</pre>

## Built With

* Front - [React](https://reactjs.org/)
* Back - [Python Flask](https://flask.palletsprojects.com/en/2.0.x/)
* Database - [Elasticsearch](https://www.elastic.co/)
* Web Server Interface - [UWSGI](https://uwsgi-docs.readthedocs.io/en/latest/)
* Reversed proxy - [NGINX](https://www.nginx.com/)
* Docker-compose


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

docker-compose and git installed

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/dimamik/what-to-read.git
   ```
2. Run docker-compose in repo
   ```sh
   cd what-to-read
   docl
   ```



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/dimamik/what-to-read/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email

Project Link: [https://github.com/dimamik/what-to-read](https://github.com/dimamik/what-to-read)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* []()
* []()
* []()





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/dimamik/repo.svg?style=for-the-badge
[contributors-url]: https://github.com/dimamik/what-to-read/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/dimamik/repo.svg?style=for-the-badge
[forks-url]: https://github.com/dimamik/what-to-read/network/members
[stars-shield]: https://img.shields.io/github/stars/dimamik/repo.svg?style=for-the-badge
[stars-url]: https://github.com/dimamik/what-to-read/stargazers
[issues-shield]: https://img.shields.io/github/issues/dimamik/repo.svg?style=for-the-badge
[issues-url]: https://github.com/dimamik/what-to-read/issues
[license-shield]: https://img.shields.io/github/license/dimamik/repo.svg?style=for-the-badge
[license-url]: https://github.com/dimamik/what-to-read/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/dimamik