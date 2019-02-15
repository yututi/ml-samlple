<template>
  <div id="app" class="section">
    <router-view/>
  </div>
</template>

<style lang="scss">
html,
body,
#app {
  height: 100%;
  width: 100%;
}
.df {
  display: flex;
  flex-direction: column;
  &.h {
    flex-direction: row;
  }
  .flex {
    flex: 1;
  }
}
.fill {
  height: 100%;
  //   width: 100%;
}

$spinnerSize: 5em;
$spinnerColor: white;

.loadingLayer {
  position: fixed;
  z-index: 100;
  opacity: 0.5;
  height: 100vh;
  width: 100vw;
  left: 0;
  top: 0;
  background-color: dimgray;
}
.is-loading {
  height: 100%;
  width: 100%;
  position: relative;
  &:after {
    content: " ";
    opacity: 1;
    position: absolute;
    border-top: 2px solid transparent;
    border-left: 2px solid transparent;
    border-right: 2px solid $spinnerColor;
    border-bottom: 2px solid $spinnerColor;
    border-radius: 100%;
    height: $spinnerSize;
    width: $spinnerSize;
    top: calc(50% - #{$spinnerSize} / 2);
    left: calc(50% - #{$spinnerSize} / 2);
    animation: roll 1s linear infinite;
  }
}

@keyframes roll {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>
