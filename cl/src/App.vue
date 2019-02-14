<template>
  <div id="app" class="section">
    <div class="container is-fluid fill">
      <div v-if="isLoading" class="loadingLayer">
        <div class="is-loading"/>
      </div>
      <div class="fill df">
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label">計測データ</label>
          </div>
          <div class="field-body">
            <div
              class="field"
              v-for="(featureName, index) in featureNameList"
              :key="featureName+'label'"
            >
              <p class="control is-expanded">
                <input
                  type="number"
                  :placeholder="featureName"
                  @input="setLavelVal(index, $event)"
                  step="0.1"
                  class="input"
                >
              </p>
            </div>
            <div class="field">
              <a class="button is-primary" @click="estimate">予測</a>
            </div>
          </div>
        </div>
        <div class="field is-horizontal flex">
          <div class="field-label is-normal">
            <label class="label">学習データ</label>
          </div>
          <div class="field-body fill">
            <table class="table is-bordered fill" style="overflow-y: scroll;display:block;">
              <thead>
                <th v-for="featureName in featureNameList" :key="featureName">
                  <abbr>{{featureName}}</abbr>
                </th>
                <th>
                  <abbr>target</abbr>
                </th>
              </thead>
              <tbody>
                <tr v-for="(training, index) in trainingList" :key="index">
                  <td
                    v-for="(featureName, featureIndex) in featureNameList"
                    :key="index+featureName"
                    @click="training.splice(featureIndex, 1, null)"
                  >{{orDefault(training[featureIndex],"--")}}</td>
                  <td>{{targetNameList[targetList[index]]}}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
    <modal ref="resultDialog"/>
  </div>
</template>

<script>
import axios from "axios";
import Modal from "./components/Modal";
export default {
  name: "app",
  components: {
    Modal: Modal
  },
  data() {
    return {
      trainingList: [],
      labelList: [],
      featureNameList: [],
      targetList: [],
      targetNames: [],
      isLoading: true
    };
  },
  methods: {
    orDefault(val, defaultVal) {
      if (val == null) {
        return defaultVal;
      }
      return val;
    },
    setLavelVal: function(index, event) {
      if (event.target.value) {
        this.labelList.splice(index, 1, event.target.value);
      } else {
        this.labelList.splice(index, 1, null);
      }
    },
    estimate: function() {
      this.isLoading = true;
      var instance = this;
      axios
        .post("api/estimate", {
          trainingSet: {
            data: instance.trainingList,
            target: instance.targetList
          },
          labels: instance.labelList
        })
        .then(response => {
          var data = response.data;
          var estimated = instance.targetNameList[data];
          instance.isLoading = false;
          instance.$refs.resultDialog.show(estimated, []);
        })
        .catch(err => {
          console.error(err);
          instance.isLoading = false;
        });
    }
  },
  mounted: function() {
    var instance = this;
    this.isLoading = true;
    axios
      .get("api/trainingSet")
      .then(response => {
        var data = response.data;
        instance.featureNameList = data.head;
        instance.trainingList = data.data;
        instance.labelList = Array(instance.featureNameList.length);
        instance.labelList.fill(null);
        instance.targetNameList = data.targetNames;
        instance.targetList = data.target;
        instance.isLoading = false;
      })
      .catch(err => {
        console.error(error);
        instance.isLoading = false;
      });
  }
};
</script>

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

.loadingLayer {
  position: fixed;
  z-index: 100;
  opacity: 0.5;
  height: 100vh;
  width: 100vw;
  left: 0;
  top: 0;
}
$spinnerSize: 5em;
$spinnerColor: white;
$spinnerBGC: dimgray;

.is-loading {
  height: 100%;
  width: 100%;
  position: relative;
  background-color: $spinnerBGC;
  &:after {
    content: " ";
    opacity: 0;
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
