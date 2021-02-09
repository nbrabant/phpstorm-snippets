# PhpStorm Live Templates (+ other settings)## Installation- Go to PhpStorm Preferences | Tools | Settings Repository- Add Read-only Source https://github.com/nbrabant/phpstorm-snippets- Restart PhpStormYou can see and manage all the snippets under the Preferences | Editor | Live Templates## Live Templates### KPN Frontend
#### lorem

```php
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
```

### PHP basics
#### trycatch
try catch body
```php
try {
    $EXPRESSION$
} catch(\Exception $e) {
    //$this->logger->error($e->getMessage());
}
```

#### dd
formatted var_dump + die
```php
echo '<pre>'; 
var_dump($EXPRESSION$); 
echo '</pre>'; 
die;
```

#### vd
vardump block
```php
<?php var_dump($EXPRESSION$); ?>
```

### Symfony
#### formhandle
Adds controller form-handling code
```php
$form = $this->createForm($CLASSNAME$::class);

$form->handleRequest($request);
if ($form->isSubmitted() && $form->isValid()) {
    // todo - do some work, like saving stuff

    $this->addFlash('success', '$SUCCESSMESSAGE$');

    return $this->redirectToRoute('$ROUTENAME$', []);
}
```

#### formrow

```php
{{ form_row(form.$FIELD$) }}
```

#### formrowfull
Renders widget/label/errors
```php
<div class="form-control">
    {{ form_label(form.$FIELD$) }}
    {{ form_widget(form.$FIELD$) }}
    {{ form_errors(form.$FIELD$) }}
</div>
```

#### repofind
Queries from a doctrine repository in a controller
```php
$this->getDoctrine()
    ->getRepository('$REPO$')->$METHOD$($ARG$);
```

#### rendertwig
Renders a Twig template from a controller
```php
return $this->render('$TEMPLATE$', [
    $END$
]);

```

#### 404unless
404 if statement for your controller
```php
if ($CONDITION$) {
    throw $this->createNotFoundException($MESSAGE$);
}
```

#### include

```php
{{ include('$TEMPLATE$') }}
```

#### method

```php
@Method("$METHOD$")
```

#### path

```php
{{ path('$ROUTE$', { $END$ }) }}
```

#### render

```php
{{ render(controller('$CONTROLLER$', { $END$ })) }}
```

#### route

```php
@Route("/$PATH$", name="$NAME$")
```

#### action
Creates a controller action.
```php
/**
 * @Route("/$PATH$", name="$ROUTE_NAME$")
 */
public function $NAME$Action()
{
    $END$
}
```

#### service
Creates a YML service
```php
$NAME$:
    class: $CLASS$
    arguments:
        - '$ARG1$'
```

#### tags
Yaml service tags
```php
tags:
    - { name: $TAGNAME$ }
```

#### createquery
Query objects in repositories with DQL
```php
$this->getEntityManager()
    ->createQuery('SELECT $ALIAS$
                   FROM $ENTITY$ $ALIAS$
                   WHERE $ALIAS$.$PROPERTY$ = :$PARAMETER$')
    ->setParameter('$PARAMETER$', $ARGUMENT$)
    ->execute();
```

#### getem
```php
$em = $this->getDoctrine()->getManager();
```

#### getrepo
```php
$em->getRepository('$ENTITY$');
```

#### doctrinecolumn
Adds a property with @ORM annotations
```php
/**
 * @var $PHPTYPE$
 *
 * @ORM\Column(name="$FIELDNAME$", type="$TYPE$")
 */
private $$$PROPERTYNAME$;
```

#### asset
```php
{{ asset('$PATH$') }}
```

#### asseticjs
```php
{% javascripts
    '$PATH$'$END$
%}
    <script type="text/javascript" src="{{ asset_url }}"></script>
{% endjavascripts %}
```

#### asseticcss
```php
{% stylesheets
    '$PATH$'$END$
    filter='cssrewrite'
%}
    <link rel="stylesheet" href="{{ asset_url }}" />
{% endstylesheets %}
```

#### xmlservices
Generates an XML services file
```php
<?xml version="1.0" ?>

<container xmlns="http://symfony.com/schema/dic/services"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://symfony.com/schema/dic/services http://symfony.com/schema/dic/services/services-1.0.xsd">

    <services>
        <service id="$SERVICEID$" class="$CLASS$" />
    </services>
</container>
```

#### yamlroute
YAML route
```php
$NAME$:
    path:   /$PATH$
    defaults:  { _controller: $CONTROLLER$ }
```

#### querybuilder
Query objects in repositories using query builder
```php
$this->createQueryBuilder('$ALIAS$')
            ->where('$ALIAS$.$PROPERTY$ = :$PARAMETER$')
            ->setParameter('$PARAMETER$', $ARGUMENT$)
            ->getQuery();
```

#### trans
Allows fast entering of translated messages
```php
{{ '$MESSAGE$'|trans }}
```

#### servix
Creates a XML service
```php
<service id="$NAME$" class="$CLASS$">
    <argument type="service" id="$ARG1$"/>
</service>
```

### Magento2 XML
#### config
Magento 2 Dependency Injection configuration
```php
<?xml version="1.0"?>
<config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:noNamespaceSchemaLocation="urn:magento:framework:ObjectManager/etc/config.xsd">
   
</config>
```

#### config_module
Magento 2 module configuration
```php
<?xml version="1.0"?>
<config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
        xsi:noNamespaceSchemaLocation="urn:magento:framework:Module/etc/module.xsd">
    <module name="$MODULE_NAME$" setup_version="0.0.0.0" />
</config>
```

#### config_system
Magento 2 System configuration
```php
<config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="urn:magento:module:Magento_Config:etc/system_file.xsd">
    <system>
        $END$
    </system>
</config>
```

#### config_acl
Magento 2 Access Level configuration
```php
<?xml version="1.0"?>
<config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
        xsi:noNamespaceSchemaLocation="urn:magento:framework:Acl/etc/acl.xsd">
    <acl>
        <resources>
            <resource id="Magento_Backend::admin">
                <resource id="$MODULE_NAMESPACE$::$HEAD$" title="$MODULE_NAME$" sortOrder="100" >
                    <resource id="$MODULE_NAMESPACE$::$RESOURCE$" title="$MODULE_NAME$" sortOrder="10">
                        <resource id="$MODULE_NAMESPACE$::$RESOURCE_SAVE$" title="$MODULE_NAME$" sortOrder="10" />
                        <resource id="$MODULE_NAMESPACE$::$RESOURCE_DELETE$" title="$MODULE_NAME$" sortOrder="20" />
                    </resource>
                </resource>
            </resource>
        </resources>
    </acl>
</config>
```

#### config_menu
Magento 2 config menu for admin panel
```php
<?xml version="1.0"?>
<config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
    xsi:noNamespaceSchemaLocation="urn:magento:module:Magento_Backend:etc/menu.xsd">
    <menu>
        <add id="$MODULE_NAMESPACE$::$HEAD$" title="$MODULE_NAME$" translate="title" module="$MODULE_NAMESPACE$" sortOrder="20" parent="Magento_Backend::$PARENT$" dependsOnModule="$MODULE_NAMESPACE$" resource="$MODULE_NAMESPACE$::$HEAD$"/>
        <add id="$MODULE_NAMESPACE$::$RESOURCE$" title="$MODULE_NAME$" translate="title" module="$MODULE_NAMESPACE$" sortOrder="10" parent="$MODULE_NAMESPACE$::$HEAD$" action="$ENDPOINT$" resource="$MODULE_NAMESPACE$::$RESOURCE$"/>
    </menu>
</config>
```

#### config_route
Magento 2 Route configuration
```php
<?xml version="1.0"?>
<config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:noNamespaceSchemaLocation="urn:magento:framework:App/etc/routes.xsd">
    <router id="admin">
        <route id="$NAME$" frontName="$NAME$">
            <module name="$MODULE_NAMESPACE$" before="Magento_Backend" />
        </route>
    </router>
</config>
```

#### config_event
Magento 2 Event xml configuration
```php
<?xml version="1.0"?>
<config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
        xsi:noNamespaceSchemaLocation="urn:magento:framework:Event/etc/events.xsd">
    <event name="$MODULE_NAME$">
        <observer name="$MODULE_NAME$" instance="$MODULE_NAMESPACE$::$CLASSNAME$"/>
    </event>
</config>
```

#### config_webapi
Magento 2 webapi xml configuration
```php
<routes xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="urn:magento:module:Magento_Webapi:etc/webapi.xsd">
    <route url="/V1/$subpath$/$methodUrl$" method="PUT">
        <service class="$vendor$\$module$\Api\$api$Interface" method="$method$"/>
        <resources>
            <resource ref="anonymous"/>
        </resources>
    </route>
</routes>
```

#### sequence
Magento 2 module sequence
```php
<sequence>
    <module name="$MODULE_NAMESPACE$"/>
</sequence>
```

#### di_preference
Magento 2 preference
```php
<preference for="$ORIGIN$" type="$OVERRIDE$" />
```

#### di_virtual_provider
Magento 2 VirtualType for provider
```php
<virtualType name="$PREFIX$GridDataProvider" type="Magento\Framework\View\Element\UiComponent\DataProvider\DataProvider">
    <arguments>
        <argument name="collection" xsi:type="object" shared="false">$RESOURCE_COLLECTION$</argument>
        <argument name="filterPool" xsi:type="object" shared="false">$PREFIX$GridFilterPool</argument> <!-- Define new object for filters -->
    </arguments>
</virtualType>
```

#### di_virtual_filter
Magento 2 VirtualType Pool for filterpool
```php
<virtualType name="$PREFIX$GridFilterPool" type="Magento\Framework\View\Element\UiComponent\DataProvider\FilterPool">
    <arguments>
        <argument name="appliers" xsi:type="array">
            <item name="regular" xsi:type="object">Magento\Framework\View\Element\UiComponent\DataProvider\RegularFilter</item>
            <item name="fulltext" xsi:type="object">Magento\Framework\View\Element\UiComponent\DataProvider\FulltextFilter</item>
        </argument>
    </arguments>
</virtualType>
```

#### di_virtual_collection
Magento 2 VirtualType for collection
```php
<virtualType name="$COLLECTION_NAMESPACE$" type="Magento\Framework\View\Element\UiComponent\DataProvider\SearchResult">
    <arguments>
        <argument name="mainTable" xsi:type="string">$TABLE_NAME$</argument>
        <argument name="resourceModel" xsi:type="string">$RESOURCE_MODEL$</argument>
    </arguments>
</virtualType>
```

#### di_type
Magento 2  Type for collection
```php
<type name="Magento\Framework\View\Element\UiComponent\DataProvider\CollectionFactory">
    <arguments>
        <argument name="collections" xsi:type="array">
            <item name="$COLLECTION_NAME$" xsi:type="string">$VIRTUAL_COLLECTION$</item>
        </argument>
    </arguments>
</type>
```

#### ui_listing
Magento 2 listing UI Component
```php
<listing xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:noNamespaceSchemaLocation="urn:magento:module:Magento_Ui:etc/ui_configuration.xsd">
         
    <!-- Integration -->
    <argument name="data" xsi:type="array">
        <item name="js_config" xsi:type="array">
            <!-- we define a provider -->
            <item name="provider" xsi:type="string">$FILE_NAME$.$FILE_NAME$_data_source</item>
        </item>
    </argument>
    
    <!-- Settings -->
    <settings>
        <buttons>
            <button name="add">
                <url path="*/*/new"/>
                <class>primary</class>
                <label translate="true">Add new $NAME$</label>
            </button>
        </buttons>
        <spinner>$FILE_NAME$_columns</spinner>
        <deps>
            <dep>$FILE_NAME$.$FILE_NAME$_data_source</dep>
        </deps>
    </settings>
    
    <!-- Data source -->
    <dataSource name="$FILE_NAME$_data_source">
        <!--@TODO : define body-->
    </dataSource>
    
    <!-- Container Listing Top -->
    <listingToolbar name="listing_top">
        <!--@TODO : define body-->
    </listingToolbar>
    
    <columns name="$FILE_NAME$_columns">
        <!--@TODO : define body-->
    </columns>
 </listing>
```

#### ui_form
Magento 2 form UI Component
```php
<form xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:noNamespaceSchemaLocation="urn:magento:module:Magento_Ui:etc/ui_configuration.xsd">

    <argument name="data" xsi:type="array">
        <item name="js_config" xsi:type="array">
            <item name="provider" xsi:type="string">$FILE_NAME$.$FILE_NAME$_data_source</item>
        </item>
        <item name="label" xsi:type="string" translate="true">$NAME$ Information</item>
        <item name="template" xsi:type="string">templates/form/collapsible</item>
    </argument>
    
    <settings>
        <buttons>
            <!-- @TODO : Complete body -->
        </buttons>
        <namespace>$FILE_NAME$</namespace>
        <dataScope>data</dataScope>
        <deps>
            <dep>$FILE_NAME$.$FILE_NAME$_data_source</dep>
        </deps>
    </settings>
    
    <dataSource name="$FILE_NAME$_data_source">
        <!--@TODO : define body-->
    </dataSource>
    
    <fieldset name="general">
        <!--@TODO : define body-->
    </fieldset>
</form>
```

#### fieldset
Magento 2 fieldset form
```php
<fieldset name="$fieldsetId$">
    <argument name="data" xsi:type="array">
        <item name="config" xsi:type="array">
            <item name="label" xsi:type="string" translate="true">$capitalizedFieldsetName$</item>
            <item name="collapsible" xsi:type="boolean">true</item>
            <item name="opened" xsi:type="boolean">false</item>
            <item name="sortOrder" xsi:type="number">$order$</item>
        </item>
    </argument>
    <!-- Add your fields here -->
    $END$
</fieldset>

```

#### field_text
Magento 2 form text input
```php
<field name="$fieldId$">
    <argument name="data" xsi:type="array">
        <item name="config" xsi:type="array">
            <item name="visible" xsi:type="boolean">true</item>
            <item name="dataType" xsi:type="string">text</item>
            <item name="label" translate="true" xsi:type="string">$capitalizedFieldName$</item>
            <item name="formElement" xsi:type="string">input</item>
            <item name="sortOrder" xsi:type="string">$order$</item>
        </item>
    </argument>
</field>
$END$
```

#### field_select
Magento 2 form text select
```php
<field name="$fieldId$">
    <argument name="data" xsi:type="array">
        <item name="options" xsi:type="object">$UiComponent$</item>
        <item name="config" xsi:type="array">
            <item name="label" translate="true" xsi:type="string">$capitalizedFieldName$</item>
            <item name="dataType" xsi:type="string">text</item>
            <item name="formElement" xsi:type="string">select</item>
            <item name="sortOrder" xsi:type="string">$order$</item>
        </item>
    </argument>
</field>
$END$
```

#### field_date
Magento 2 form date input
```php
<field name="$fieldId$">
    <argument name="data" xsi:type="array">
        <item name="config" xsi:type="array">
            <item name="label" translate="true" xsi:type="string">$capitalizedFieldName$</item>
            <item name="visible" xsi:type="boolean">true</item>
            <item name="dataType" xsi:type="string">text</item>
            <item name="formElement" xsi:type="string">date</item>
            <item name="sortOrder" xsi:type="string">$order$</item>
            <item name="validation" xsi:type="array">
                <item name="validate-date" xsi:type="boolean">true</item>
            </item>
        </item>
    </argument>
</field>
$END$
```

#### field_file
Magento 2 form file input
```php
<field name="$fieldName$">
    <argument name="data" xsi:type="array">
        <item name="config" xsi:type="array">
            <!--<item name="label" translate="true" xsi:type="string">$capitalizedFieldName$</item>-->
            <item name="formElement" xsi:type="string">fileUploader</item>
            <item name="componentType" xsi:type="string">fileUploader</item>
            <item name="notice" xsi:type="string" translate="true">Allowed file types: jpeg, gif, png</item>
            <item name="maxFileSize" xsi:type="number">2097152</item>
            <item name="allowedExtensions" xsi:type="string">jpg jpeg gif png</item>
            <item name="uploaderConfig" xsi:type="array">
                <item name="url" xsi:type="string">$routeId$/file/uploader</item>
            </item>
            <item name="sortOrder" xsi:type="string">$order$</item>
        </item>
    </argument>
</field>
$END$
```

#### field_hidden
Magento 2 form hidden input
```php
<field name="$fieldName$">
    <argument name="data" xsi:type="array">
        <item name="config" xsi:type="array">
            <item name="visible" xsi:type="boolean">true</item>
            <item name="dataType" xsi:type="string">number</item>
            <item name="formElement" xsi:type="string">hidden</item>
            <item name="sortOrder" xsi:type="string">$order$</item>
        </item>
    </argument>
</field>
$END$
```

#### field_wysiwyg
Magento 2 form wisiwyg input
```php
<field name="$fieldName$"><!-- Do not use "-" on the field name. It breaks the WYSIWYG -->
    <argument name="data" xsi:type="array">
        <item name="config" xsi:type="array">
            <item name="label" xsi:type="string">$capitalizedFieldName$</item>
            <item name="sortOrder" xsi:type="number">$order$</item>
            <item name="formElement" xsi:type="string">wysiwyg</item>
            <item name="wysiwyg" xsi:type="boolean">true</item>
            <item name="wysiwygConfigData" xsi:type="array">
                <item name="hidden" xsi:type="boolean">false</item>
                <item name="settings" xsi:type="array">
                    <item name="theme_advanced_buttons1" xsi:type="string">bold,italic,|,justifyleft,justifycenter,justifyright,|,fontselect,fontsizeselect,|,forecolor,backcolor,|,link,unlink,|,bullist,numlist,|,code</item>
                    <item name="theme_advanced_buttons2" xsi:type="boolean">false</item>
                    <item name="theme_advanced_buttons3" xsi:type="boolean">false</item>
                    <item name="theme_advanced_buttons4" xsi:type="boolean">false</item>
                    <item name="theme_advanced_statusbar_location" xsi:type="boolean">false</item>
                </item>
                <item name="files_browser_window_url" xsi:type="boolean">false</item>
                <item name="height" xsi:type="string">100px</item>
                <item name="toggle_button" xsi:type="boolean">false</item>
                <item name="add_widgets" xsi:type="boolean">false</item>
                <item name="add_variables" xsi:type="boolean">false</item>
                <item name="add_images" xsi:type="boolean">false</item>
            </item>
            <item name="template" xsi:type="string">ui/form/field</item>
            <item name="additionalClasses" xsi:type="string">admin__field-wide</item>
        </item>
    </argument>
</field>
$END$
```

#### field_boolean
Magento 2 form boolean input
```php
<field name="$fieldName$">
    <argument name="data" xsi:type="array">
        <item name="config" xsi:type="array">
            <item name="sortOrder" xsi:type="number">$order$</item>
            <item name="dataType" xsi:type="string">boolean</item>
            <item name="formElement" xsi:type="string">checkbox</item>
            <item name="prefer" xsi:type="string">toggle</item>
            <item name="label" xsi:type="string" translate="true">$capitalizedFieldName$</item>
            <item name="valueMap" xsi:type="array">
                <item name="true" xsi:type="string">1</item>
                <item name="false" xsi:type="string">0</item>
            </item>
            <item name="validation" xsi:type="array">
                <item name="required-entry" xsi:type="boolean">false</item>
            </item>
            <item name="default" xsi:type="string">1</item>
        </item>
    </argument>
</field>
$END$
```

#### layout
Magento 2 layout
```php
<?xml version="1.0"?>
<page xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
        xsi:noNamespaceSchemaLocation="urn:magento:framework:View/Layout/etc/page_configuration.xsd">
    <body>
        <referenceContainer name="content">
            <block class="$Class$" name="$Name$"/>
        </referenceContainer>
    </body>
</page>
```

#### layout_referenceContainer
Magento 2 layout reference container
```php
<referenceContainer name="$containerName$">
    </referenceContainer>
```

#### layout_referenceBlock
Magento 2 layout reference block
```php
<referenceBlock name="$blockName$">
    </referenceBlock>
```

#### layout_block
Magento 2 layout block
```php
<block class="$blockClass$" name="$blockName$"
    template="$blockTemplate$" />
```

#### layout_disable_component
Magento 2 layout component disabling
```php
<referenceBlock name="$blockName$">
    <arguments>
        <argument name="jsLayout" xsi:type="array">
            <item name="components" xsi:type="array">
                <item name="$componentName$" xsi:type="array">
                    <item name="config" xsi:type="array">
                        <item name="componentDisabled" xsi:type="boolean">true</item>
                    </item>
                </item>
            </item>
        </argument>
    </arguments>
</referenceBlock>
```

