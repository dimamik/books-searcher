import {createGlobalStyle} from "styled-components"

export const GlobalStyles = createGlobalStyle`


  body, html {
    background: ${({theme}) => theme.background};
    color: ${({theme}) => theme.text};
    font-family: 'Montserrat', sans-serif;
    transition: all 0.50s ease-out;
    text-align: center;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }

  .fp-tableCell {
    vertical-align: baseline;
  }

  // Navbar styling

  #fp-nav.fp-right {
    right: 2vh;

  }

  @media only screen and (max-width: 600px) {
    #fp-nav.fp-right {
      right: -1.5vw;
    }

  }


  #fp-nav ul li a span, .fp-slidesNav ul li a span {
    background: ${props => props.theme.text};
  }

`
