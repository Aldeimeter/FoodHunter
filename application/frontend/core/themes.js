// themes.js
const palette = {
  earthyBrown: '#AB6E3E', // Reminiscent of grains and baked goods
  leafyGreen: '#4CAF50', // Fresh, vibrant greens of vegetables
  tomatoRed: '#E53935', // Bright, inviting tomato red
  creamyWhite: '#FFF8E1', // Off-white like cream or soft cheese
  deepBlue: '#303F9F', // Dark blue for a contrasting color
  charcoalGray: '#424242', // Neutral dark tone for dark theme background
  cloudGray: '#ECEFF1', // Soft light gray for light theme background
};

export const theme = {
  isDark: false,
  colors: {
    background: palette.cloudGray,
    foreground: palette.charcoalGray,
    primary: palette.earthyBrown,
    secondary: palette.creamyWhite,
    success: palette.leafyGreen,
    danger: palette.tomatoRed,
    warning: palette.deepBlue, // Consider using this for less critical alerts or info
  },
  spacing: {
    s: 8,
    m: 16,
    l: 24,
    xl: 40,
  },
  textVariants: {
    header: {
      fontFamily: 'merriweather-regular',
      fontSize: 36,
      fontWeight: 'bold',
    },
    body: {
      fontFamily: 'merriweather-regular',
      fontSize: 16,
    },
  }
};

export const darkTheme = {
  ...theme,
  isDark: true,
  colors: {
    background: palette.charcoalGray,
    foreground: palette.creamyWhite,
    primary: palette.earthyBrown,
    secondary: palette.creamyWhite,
    success: palette.leafyGreen,
    danger: palette.tomatoRed,
    warning: palette.deepBlue,
  }
};
