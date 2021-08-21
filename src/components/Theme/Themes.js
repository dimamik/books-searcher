const baseTheme = {
//    Add base properties to control the app flow
//    Define Some variables to use further
}

export const lightTheme = {
    ...baseTheme,
    themeName: 'lightTheme',
    body: '#FFF',
    text: '#363537',
    toggleBorder: '#FFF',
    background: '#f0dec6',
    dividerColor: 'black'

}
export const darkTheme = {
    ...baseTheme,
    body: '#363537',
    themeName: 'darkTheme',
    text: '#ffffff',
    toggleBorder: '#2b2b2c',
    background: 'black',
    searchBackground: '#a49788',
    dividerColor: 'white'

}

