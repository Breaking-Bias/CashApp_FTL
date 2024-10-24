module.exports = {
    preset: 'ts-jest',
    testEnvironment: 'jsdom',
    setupFilesAfterEnv: ['<rootDir>/src/setupTests.ts'],
    transform: {
        '^.+\\.tsx?$': 'ts-jest', // Ensure TypeScript files are transformed
        '^.+\\.jsx?$': 'babel-jest', // Use babel-jest for JavaScript and JSX files
    },
    moduleNameMapper: {
        '\\.(css|less|scss|sass)$': 'identity-obj-proxy', // Handle CSS modules if needed
    },
};