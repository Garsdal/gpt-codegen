<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<!-- PROJECT LOGO -->
<h3 align="center">GPT Codegen</h3>

  <p align="center">
    This code can be used to continue develop no-code applications based on ChatGPT API and prompt engineering. The current implementation is only focused on dynamic parsing of dataframes from any to standardized format.
    <br />
    <a href="https://github.com/Garsdal/gpt-codegen"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Garsdal/gpt-codegen">View Demo</a>
    ·
    <a href="https://github.com/Garsdal/gpt-codegen/issues">Report Bug</a>
    ·
    <a href="https://github.com/Garsdal/gpt-codegen/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
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
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://github.com/Garsdal/gpt-codegen)

<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

Set up Python version 3.7 or higher

### Installation

1. Get a OpenAI API Key at [https://openai.com/product/](https://openai.com/product)
2. Clone the repo
   ```sh
   git clone https://github.com/Garsdal/gpt-codegen.git
   ```
3. Create a new virtual environment and install the requirements
   ```sh
   pip install -r requirements.txt
   ```
4. Install the package
   ```sh
   pip install -e .
   ```
5. Enter your OpenAI API key in `config/config_api.json`
   ```json
   {
    "API_KEY": "YOUR KEY HERE",
   }
   ```
   Alternatively, this can also be done through the CLI, by calling
   ```py
   python src/cli.py config-api --key <YOUR_API_KEY>
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] ???
- [ ] ???
- [ ] ???

See the [open issues](https://github.com/Garsdal/gpt-codegen/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Marcus Garsdal - [LinkedIn](https://www.linkedin.com/in/marcus-garsdal/) - garsdal@live.dk

Project Link: [https://github.com/Garsdal/gpt-codegen](https://github.com/Garsdal/gpt-codegen)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Thanks to othneildrew for the README template.
* [https://github.com/othneildrew/](https://github.com/othneildrew/)

Thanks to OpenAI for giving personal access to their API for projects like these.
* [https://openai.com/](https://openai.com/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Garsdal/spotify-tracklist-generator.svg?style=for-the-badge
[contributors-url]: https://github.com/Garsdal/gpt-codegen/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Garsdal/spotify-tracklist-generator.svg?style=for-the-badge
[forks-url]: https://github.com/Garsdal/gpt-codegen/network/members
[stars-shield]: https://img.shields.io/github/stars/Garsdal/spotify-tracklist-generator.svg?style=for-the-badge
[stars-url]: https://github.com/Garsdal/gpt-codegen/stargazers
[issues-shield]: https://img.shields.io/github/issues/Garsdal/spotify-tracklist-generator.svg?style=for-the-badge
[issues-url]: https://github.com/Garsdal/gpt-codegen/issues
[license-shield]: https://img.shields.io/github/license/Garsdal/spotify-tracklist-generator.svg?style=for-the-badge
[license-url]: https://github.com/Garsdal/gpt-codegen/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/marcus-garsdal
[product-screenshot]: assets/robot.png