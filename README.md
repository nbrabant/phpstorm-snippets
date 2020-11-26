# PhpStorm Live Templates (+ other settings)## Installation- Go to PhpStorm Preferences | Tools | Settings Repository- Add Read-only Source https://github.com/nbrabant/phpstorm-snippets- Restart PhpStormYou can see and manage all the snippets under the Preferences | Editor | Live Templates## Live Templates### Magento2 XML
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

#### page_layout
Magento layout
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

### KPN Frontend
#### lorem

```php
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
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

