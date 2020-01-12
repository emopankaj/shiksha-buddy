<template>
    <b-row v-if="order===1" class="align-items-center">
        <b-col v-for="menuItem in menuStructure" :key="'column_' + menuItem.id" cols="6" sm="4" md="2" xl
               class="mb-3 mb-xl-0">
            <b-button block variant="outline-primary"
                      class="item mt-2" @click="() => editMenuItem(menuItem)">
                {{menuItem.label}}
            </b-button>
            <nested-draggable v-if="menuItem.menus" :menu="menuItem.menus" :order="order+1"/>
        </b-col>
    </b-row>
    <draggable v-else-if="order===2" v-model="menuStructure" :group="{name:'g1'}">
        <div v-for="menuItem in menuStructure" :key="'second_order_' + menuItem.id">
            <b-button block variant="warning"
                      class="item mt-2 ml-4 w-fill-available" @click="() => editMenuItem(menuItem)">
                {{menuItem.label}}
            </b-button>
            <nested-draggable v-if="menuItem.menus" :menu="menuItem.menus" :order="order+1"/>
        </div>
    </draggable>
    <draggable v-else v-model="menuStructure" :group="{name:'g1'}">
        <b-button v-for="menuItem in menuStructure"
                  :key="'third_order_' + menuItem.id"
                  block variant="danger"
                  class="item mt-2 ml-5 w-fill-available" @click="() => editMenuItem(menuItem)">
            {{menuItem.label}}
        </b-button>
    </draggable>
</template>

<script>
    import draggable from "vuedraggable";
    import {EventBus} from "@/main";

    export default {
        name: "nested-draggable",
        components: {
            draggable
        },
        props: {
            menu: {
                required: true,
                type: Array
            },
            order: {
                type: Number
            }
        },
        data() {
            return {menuStructure: this.menu}
        },
        methods: {
            editMenuItem(currentMenuItem) {
                EventBus.$emit('edit-menu-item', currentMenuItem);
            }
        }


    };
</script>

<style scoped>
    .w-fill-available {
        width: -webkit-fill-available;
    }
</style>
