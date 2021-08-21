import React, {useContext} from 'react'
import {func} from 'prop-types';
import styled, {ThemeContext} from "styled-components"
import {FaToggleOff, FaToggleOn} from 'react-icons/fa';
import {Button, Fade, Tooltip} from "@material-ui/core";

const StyledToggler = styled(Button)`
  color: ${props => props.theme.text};
`;

const TogglerDiv = styled.div`
  position: fixed;
  display: block;
  z-index: 100;
  right: 0;
`

const iconStyles = {
    height: '100%',
    width: '100%'
}

const ThemeToggler = ({switchTheme}) => {
    //Theme also can be passed via themeContext prop from parent
    const themeContext = useContext(ThemeContext);

    let isLightTheme = themeContext.themeName === 'lightTheme';

    return (
        <TogglerDiv>
            <Tooltip
                title={
                    isLightTheme ? 'Dark mode' : 'Light mode'
                }
                TransitionComponent={Fade} TransitionProps={{timeout: 600}}
            >
                <StyledToggler onClick={switchTheme}>
                    {
                        isLightTheme ? <FaToggleOn style={iconStyles}/> :
                            <FaToggleOff style={iconStyles}/>
                    }

                </StyledToggler>
            </Tooltip>
        </TogglerDiv>

    );
};
ThemeToggler.propTypes = {
    switchTheme: func.isRequired
}
export default ThemeToggler;
