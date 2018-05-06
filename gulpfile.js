const
    gulp = require('gulp'),
    concat = require('gulp-concat'),
    uglify = require('gulp-uglify-es').default,
    cleanCSS = require('gulp-clean-css'),
    minifyCSS = require('gulp-minify-css'),
    less = require('gulp-less'),
    fs = require('fs'),
    rename = require("gulp-rename"),
    path = require('path');


let frontendSettings = JSON.parse(fs.readFileSync('frontend-settings.json', 'utf8'));

gulp.task('core-less', function () {
    let lessList = frontendSettings['client_less'];
    for (let i = 0; i < lessList.length; i++) {
        lessList[i] = './static' + lessList[i];
    }

    return gulp.src(lessList)
        .pipe(less({
            paths: [path.join(__dirname, 'less', 'includes')]
        }))
        .pipe(cleanCSS())
        .pipe(minifyCSS({
            keepBreaks: true
        }))
        .pipe(rename({suffix: ".min"}))
        .pipe(gulp.dest('./static/core/dist'));
});

gulp.task('core-js', function () {
    let jsList = frontendSettings['client_js'];
    for (let i = 0; i < jsList.length; i++) {
        jsList[i] = './static' + jsList[i];
    }

    return gulp.src(jsList)
        .pipe(concat('core.min.js'))
        .pipe(uglify())
        .pipe(gulp.dest('./static/core/dist'));
});

gulp.task('default', ['core-less', 'core-js']);