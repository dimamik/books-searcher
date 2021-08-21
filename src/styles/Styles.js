import styled, {keyframes} from "styled-components";
import Paper from "@material-ui/core/Paper";
import {zoomIn} from "react-animations";
import InputBase from "@material-ui/core/InputBase";
import {ListItem} from "@material-ui/core";


// Fonts

export const StyledH1 = styled.h1`
  font-weight: 900;
  font-size: x-large;
`
export const StyledHeader = styled.p`
  color: ${({theme}) => theme.text};
  font-weight: 700;
  font-size: 1rem;
  font-family: inherit;
`

export const StyledItalic = styled.p`
  font-style: italic;
  font-size: 1rem;
  font-weight: 500;
`

export const StyledNormal = styled.p`
  font-family: inherit;
  font-weight: 400;
  font-size: 1rem;
  max-height: 6vh;
`

// Elements

export const StyledPaper = styled(Paper)`
  background-color: ${props => props.theme.searchBackground};
  height: 100%;
  border-radius: 50px;
`
const bounceAnimation = keyframes`${zoomIn}`;
export const ZoomedInDiv = styled.div`
  animation: 1s ${bounceAnimation};
  height: 100%;
  display: flex;
  justify-content: center; /* align horizontal */
  align-items: center /* align vertical */
`

export const StyledInputBase = styled(InputBase)`
  color: ${props => props.theme.text};
  opacity: 1;
  width: 100%;
`

export const StyledListItem = styled(ListItem)`
  border-top: 1px solid ${props => props.theme.dividerColor};
  width: 100%;
  box-shadow: rgba(0, 0, 0, 0.1) 0 4px 6px -1px, rgba(0, 0, 0, 0.06) 0px 2px 4px -1px;
`