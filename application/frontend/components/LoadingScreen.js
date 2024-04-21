import React from 'react';
import { View, ActivityIndicator, StyleSheet, Text } from 'react-native';
// Language stuff
import { useTranslation } from 'react-i18next';
// Theme stuff
import { useTheme } from '../core/ThemeContext';

const LoadingScreen = () => {
    const { theme } = useTheme();

    const styles = createStyles(theme);

    const {t} = useTranslation();
    return (
      <View style={styles.container}>
          <ActivityIndicator size="large" color={theme.colors.secondary} />
          <Text>{t('LOADING')}</Text>
      </View>
    );
};

const createStyles = (theme) => StyleSheet.create({
    container: {
        position: 'absolute',
        left: 0,
        right: 0,
        top: 0,
        bottom: 0,
        alignItems: 'center',
        justifyContent: 'center',
        backgroundColor: 'rgba(0, 0, 0, 0.5)' // Semi-transparent background
    }
});

export default LoadingScreen;
