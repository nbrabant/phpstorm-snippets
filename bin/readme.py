# based on https://github.com/knpuniversity/phpstorm-settings

import xml.etree.ElementTree as etree
import os

readmeFile = open("README.md", "w")
readmeFile.write("# PhpStorm Live Templates (+ other settings)\r")
readmeFile.write("## Installation\r")
readmeFile.write("- Go to PhpStorm Preferences | Tools | Settings Repository\r")
readmeFile.write("- Add Read-only Source https://github.com/nbrabant/phpstorm-snippets\r")
readmeFile.write("- Restart PhpStorm\r\r")
readmeFile.write("You can see and manage all the snippets under the Preferences | Editor | Live Templates\r")
readmeFile.write("## Live Templates\r")

filenames = os.listdir('templates')
for filename in filenames:
    
    tree = etree.parse("templates/" + filename) 
    templateSet = tree.getroot()

    readmeFile.write("### " + templateSet.attrib['group'] + "\n")

    for templateElement in templateSet:

        template = templateElement.attrib['value']
# <context>
#     <option name="XML" value="true" />
# </context>
        readmeFile.write("#### " + templateElement.attrib['name'] + "\n")
        if "description" in templateElement.attrib:
            readmeFile.write(templateElement.attrib['description'] + "\n")
        readmeFile.write("```php\n" + template + "\n```\n\n")

readmeFile.close()

# //     foreach ($element->template as $templateElement) {
# //         $template = (string)$templateElement->attributes()->value;
# //         $name = (string)$templateElement->attributes()->name;
# //         $description = (string)$templateElement->attributes()->description;

# //         $md .= sprintf("```php\n%s\n```\n\n", $template);
# //     }